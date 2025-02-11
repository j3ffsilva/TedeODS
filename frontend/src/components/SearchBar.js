import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { buscarTrabalhos, buscarODS } from '../api';

// Estilos
const SearchWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 150px;
`;

const SearchInput = styled.input`
  width: 600px;
  padding: 15px;
  font-size: 18px;
  border: 2px solid #ddd;
  border-radius: 24px;
  margin-bottom: 20px;
`;

const SearchButton = styled.button`
  padding: 10px 20px;
  background-color: #4285f4;
  color: white;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-size: 16px;

  &:hover {
    background-color: #357ae8;
  }
`;

const TagsWrapper = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 20px 0;
`;

const Tag = styled.span`
  background-color: ${({ color }) => color || '#f1f3f4'};
  color: #fff;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  cursor: pointer;

  &:hover {
    opacity: 0.8;
  }
`;

const FeedbackMessage = styled.p`
  color: red;
  margin-top: 20px;
`;

// Função para normalizar texto (remover acentos, transformar em minúsculas)
const normalizarTexto = (texto) =>
  texto
    .normalize('NFD') // Normaliza acentos
    .replace(/[\u0300-\u036f]/g, '') // Remove acentos
    .toLowerCase(); // Converte para minúsculas

    function SearchBar({ query, onResults }) {
      const [inputValue, setInputValue] = useState(''); // Estado para o campo de entrada
      const [loading, setLoading] = useState(false);
      const [error, setError] = useState(null);
      const [tags, setTags] = useState([]); // Todas as tags disponíveis
      const [currentTags, setCurrentTags] = useState([]); // Tags rotativas exibidas
      const [tagColors, setTagColors] = useState([]); // Cores rotativas
      const [feedback, setFeedback] = useState('');
    
      const fixedColors = ['#FF5733', '#4285F4', '#FFA500', '#34A853', '#800080'];
    
      // Atualiza o valor do campo quando o `query` muda
      useEffect(() => {
        if (query) {
          setInputValue(query); // Preenche o campo com o valor do `query`
          handleSearch(query); // Realiza a busca automaticamente
        }
      }, [query]);
    
      // Função para carregar as tags
      useEffect(() => {
        const carregarODS = async () => {
          try {
            const resultados = await buscarODS();
            const uniqueTags = [...new Set(resultados.flatMap((item) => item.palavras_chave || []))];
            setTags(uniqueTags); // Salva todas as tags disponíveis
            atualizarTags(uniqueTags); // Inicializa as primeiras tags exibidas
            setTagColors([...fixedColors].sort(() => Math.random() - 0.5));
          } catch (err) {
            console.error('Erro ao carregar dados iniciais:', err);
            setError('Erro ao carregar dados iniciais.');
          }
        };
    
        carregarODS();
      }, []);
    
      // Função para atualizar as tags exibidas a cada 20 segundos
      useEffect(() => {
        if (tags.length > 0) {
          const interval = setInterval(() => {
            atualizarTags(tags);
          }, 20000); // 20 segundos
    
          return () => clearInterval(interval); // Limpa o intervalo ao desmontar
        }
      }, [tags]);
    
      const atualizarTags = (todasAsTags) => {
        const shuffledTags = [...todasAsTags].sort(() => Math.random() - 0.5);
        setCurrentTags(shuffledTags.slice(0, 5)); // Exibe as próximas 5 tags
        setTagColors([...fixedColors].sort(() => Math.random() - 0.5));
      };
    
      const handleSearch = async (searchQuery = inputValue) => {
        setLoading(true);
        setError(null);
        setFeedback('');
    
        const identificarTipoDeBusca = (query) => {
          const lowerQuery = normalizarTexto(query.trim());
    
          if (lowerQuery.startsWith('data:')) {
            const data = lowerQuery.replace('data:', '').trim();
            return { tipo: 'data', valor: data };
          }
    
          if (lowerQuery.startsWith('ods:')) {
            const ods = lowerQuery.replace('ods:', '').trim();
            return { tipo: 'ods', valor: parseInt(ods, 10) };
          }
    
          return { tipo: 'palavra-chave', valor: query };
        };
    
        const { tipo, valor } = identificarTipoDeBusca(searchQuery);
    
        try {
          let resultados = [];
    
          if (tipo === 'data') {
            const params = valor.length === 4 ? { data: `${valor}-01-01` } : { data: valor };
            resultados = await buscarTrabalhos(params);
          } else if (tipo === 'ods') {
            const params = { ods: valor };
            resultados = await buscarTrabalhos(params);
          } else if (tipo === 'palavra-chave') {
            const termos = normalizarTexto(valor).split(/\s+/);
            const buscas = await Promise.all(
              termos.map((termo) =>
                buscarTrabalhos({ palavra_resumo: termo }).catch(() => [])
              )
            );
            resultados = [...new Set(buscas.flat())];
          }
    
          if (resultados.length === 0) {
            setFeedback('Nenhum resultado encontrado. Tente outros termos ou refine sua busca.');
          }
          onResults(resultados);
        } catch (err) {
          setError('Erro ao buscar trabalhos. Tente novamente.');
          console.error(err);
        } finally {
          setLoading(false);
        }
      };
    
      const handleTagClick = (tag) => {
        setInputValue(tag);
        handleSearch(tag);
      };
    
      const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
          handleSearch();
        }
      };
    
      return (
        <SearchWrapper>
          <SearchInput
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ex.: data:2021, ODS:1, dignidade previdência"
          />
          <SearchButton onClick={() => handleSearch()} disabled={loading}>
            {loading ? 'Buscando...' : 'Pesquisar'}
          </SearchButton>
          {error && <FeedbackMessage>{error}</FeedbackMessage>}
          {feedback && <FeedbackMessage>{feedback}</FeedbackMessage>}
          
          <TagsWrapper>
            {currentTags.map((tag, index) => (
              <Tag
                key={index}
                onClick={() => handleTagClick(tag)}
                color={tagColors[index % tagColors.length]}
              >
                {tag}
              </Tag>
            ))}
          </TagsWrapper>
        </SearchWrapper>
      );
    }
    
    export default SearchBar;
    