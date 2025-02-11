import React from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import styled from 'styled-components';

const PageWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
`;

const HeaderWrapper = styled.header`
  width: 100%;
  padding: 20px 0;
  background-color: #f8f9fa;
  box-shadow: 0 4px 2px -2px gray;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  position: sticky;
  top: 0;
  z-index: 1000;
`;

const Logo = styled.div`
  font-size: 24px;
  font-weight: bold;
  color: #333;
`;

const SearchBarWrapper = styled.div`
  display: flex;
  gap: 10px;

  input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border: 2px solid #ddd;
    border-radius: 24px;
    width: 300px;
  }

  button {
    padding: 10px 20px;
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 24px;
    cursor: pointer;

    &:hover {
      background-color: #357ae8;
    }
  }
`;

const ContentWrapper = styled.div`
  max-width: 800px;
  width: 100%;
  margin-top: 20px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

  h1 {
    color: #1a73e8;
  }

  p {
    color: #555;
    line-height: 1.6;
  }

  small {
    color: #888;
  }
`;

const BackButton = styled.button`
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4285f4;
  color: white;
  border: none;
  border-radius: 24px;
  cursor: pointer;

  &:hover {
    background-color: #357ae8;
  }
`;

function Detalhes() {
  const navigate = useNavigate();
  const { id } = useParams();

  // Simular a busca do item por ID (ajuste com a lógica correta para o seu app)
  const result = JSON.parse(localStorage.getItem('selectedResult'));

  if (!result) {
    return <p>Erro: Detalhes não encontrados.</p>;
  }

  return (
    <PageWrapper>
      {/* Header com busca integrada */}
      <HeaderWrapper>
        <Logo>ODS</Logo>
        <SearchBarWrapper>
          <input
            type="text"
            placeholder="Digite sua busca..."
            onKeyDown={(e) => {
              if (e.key === 'Enter') navigate('/');
            }}
          />
          <button onClick={() => navigate('/')}>Buscar</button>
        </SearchBarWrapper>
      </HeaderWrapper>

      {/* Conteúdo */}
      <ContentWrapper>
        <h1>{result.titulo}</h1>
        <p>{result.resumo}</p>
        <small>Data: {result.data}</small>
        <p>ODS: {result.ODS.join(', ')}</p>
      </ContentWrapper>

      {/* Botão Voltar */}
      <BackButton onClick={() => navigate('/')}>Voltar</BackButton>
    </PageWrapper>
  );
}

export default Detalhes;
