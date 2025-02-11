import React, { useRef, useEffect } from 'react';
import styled from 'styled-components';

const HeaderWrapper = styled.header`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #f8f9fa;
  padding: 20px 0;
  box-shadow: 0 4px 2px -2px gray;
  z-index: 1000;
`;

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
`;

const Logo = styled.div`
  font-size: 24px;
  font-weight: bold;
  color: #333;
`;

const DropdownWrapper = styled.div`
  position: relative;
`;

const DropdownButton = styled.button`
  background-color: #4285f4;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background-color: #357ae8;
  }
`;

const DropdownMenu = styled.ul`
  position: absolute;
  top: 100%;
  left: 0;
  background: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
  margin: 0;
  padding: 10px 0;
  border-radius: 5px;
  display: ${({ open }) => (open ? 'block' : 'none')};
  z-index: 100;
  width: 200px;
`;

const DropdownItem = styled.li`
  padding: 5px 20px;
  cursor: pointer;
  color: #333;

  &:hover {
    background-color: #f1f1f1;
  }
`;

function Header({ onODSSelect }) {
  const [dropdownOpen, setDropdownOpen] = React.useState(false);
  const dropdownRef = useRef(null); // Para capturar cliques fora do menu

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  const handleODSClick = (ods) => {
    onODSSelect(`ODS:${ods}`); // Passa a ODS selecionada como query para o SearchBar
    setDropdownOpen(false); // Fecha o dropdown
  };

  // Fecha o menu ao clicar fora
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setDropdownOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  return (
    <HeaderWrapper>
      <Container>
        <Logo>ODS</Logo>
        <DropdownWrapper ref={dropdownRef}>
          <DropdownButton onClick={toggleDropdown}>
            Selecionar ODS
          </DropdownButton>
          <DropdownMenu open={dropdownOpen}>
            {[...Array(16)].map((_, index) => (
              <DropdownItem
                key={index + 1}
                onClick={() => handleODSClick(index + 1)}
              >
                ODS {index + 1}
              </DropdownItem>
            ))}
          </DropdownMenu>
        </DropdownWrapper>
      </Container>
    </HeaderWrapper>
  );
}

export default Header;
