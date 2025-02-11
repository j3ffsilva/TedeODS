import React, { useState } from "react";
import styled from "styled-components";

const ResultsWrapper = styled.div`
  max-width: 800px;
  margin: 20px auto;
`;

const ResultItem = styled.div`
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;

  h3 {
    margin: 0;
    color: #1a73e8;
  }

  p {
    margin: 10px 0;
    color: #555;
  }

  small {
    color: #888;
    display: block;
    margin-top: 10px;
  }
`;

const PaginationWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  gap: 5px;

  button {
    padding: 10px 15px;
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;

    &:disabled {
      background-color: #ddd;
      cursor: not-allowed;
    }

    &:hover:not(:disabled) {
      background-color: #357ae8;
    }
  }
`;

function SearchResults({ results }) {
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 5;

  const totalPages = Math.ceil(results.length / itemsPerPage);
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  const handleNext = () => setCurrentPage((prev) => Math.min(prev + 1, totalPages));
  const handlePrevious = () => setCurrentPage((prev) => Math.max(prev - 1, 1));
  const handleJumpToStart = () => setCurrentPage(1);
  const handleJumpToEnd = () => setCurrentPage(totalPages);

  if (results.length === 0) return null;

  return (
    <>
      <ResultsWrapper>
        {results.slice(startIndex, endIndex).map((result, index) => (
          <ResultItem key={index}>
            <h3>{result.titulo}</h3>
            <p>{result.resumo}</p>
            <small>Data: {result.data}</small>
            <small>ODS: {result.ODS.join(", ")}</small>
          </ResultItem>
        ))}
      </ResultsWrapper>
      <PaginationWrapper>
        <button onClick={handleJumpToStart} disabled={currentPage === 1}>
          {"<<"}
        </button>
        <button onClick={handlePrevious} disabled={currentPage === 1}>
          {"<"}
        </button>
        <span>
          Página {currentPage} de {totalPages}
        </span>
        <button onClick={handleNext} disabled={currentPage === totalPages}>
          {">"}
        </button>
        <button onClick={handleJumpToEnd} disabled={currentPage === totalPages}>
          {">>"}
        </button>
      </PaginationWrapper>
    </>
  );
}

export default SearchResults;
