import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import SearchBar from './components/SearchBar';
import SearchResults from './components/SearchResults';
import styled from 'styled-components';

const AppWrapper = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const MainContent = styled.main`
  flex: 1;
  padding-bottom: 80px;
`;

function App() {
  const [results, setResults] = useState([]);
  const [query, setQuery] = useState(''); // Adicionamos um estado para o query

  const handleODSSelect = (odsQuery) => {
    setQuery(odsQuery); // Atualiza o estado do query ao selecionar uma ODS
  };

  return (
    <AppWrapper>
      <Header onODSSelect={handleODSSelect} />
      <MainContent>
        <SearchBar query={query} onResults={setResults} />
        <SearchResults results={results} />
      </MainContent>
      <Footer />
    </AppWrapper>
  );
}


export default App;
