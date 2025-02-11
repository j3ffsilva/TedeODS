import React from 'react';
import styled from 'styled-components';

const FooterWrapper = styled.footer`
  background-color: #f8f9fa;
  color: #333;
  text-align: center;
  padding: 20px 0;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
`;

function Footer() {
  return (
    <FooterWrapper>
      <p>© 2024 - Sistema de Pesquisa ODS</p>
    </FooterWrapper>
  );
}

export default Footer;
