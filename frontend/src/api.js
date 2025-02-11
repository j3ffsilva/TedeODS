export async function buscarTrabalhos(params) {
  const queryString = new URLSearchParams(params).toString();
  try {
    const response = await fetch(`/buscar?${queryString}`);
    if (!response.ok) {
      console.error('Erro no fetch:', response.status, response.statusText);
      throw new Error(`Erro ao buscar trabalhos: ${response.statusText}`);
    }
    return response.json();
  } catch (error) {
    console.error('Erro ao buscar dados:', error);
    throw error;
  }
}

export async function buscarODS() {
  try {
    const response = await fetch(`/buscar?ods=1`);
    if (!response.ok) {
      console.error('Erro no fetch:', response.status, response.statusText);
      throw new Error(`Erro ao buscar ODS: ${response.statusText}`);
    }
    return response.json();
  } catch (error) {
    console.error('Erro ao buscar dados ODS:', error);
    throw error;
  }
}





//Localhost abaixo:
// const BASE_URL = ''; // Proxy irá tratar do domínio

// export async function buscarTrabalhos(params) {
//   const queryString = new URLSearchParams(params).toString();
//   //const response = await fetch(`${BASE_URL}/buscar?${queryString}`); Localhost
//   const response = await fetch(`/buscar?${queryString}`); //EM produção
  
//   if (!response.ok) {
//     throw new Error(`Erro ao buscar trabalhos: ${response.statusText}`);
//   }

//   return response.json();
// }

// export async function buscarODS() {
//   const response = await fetch(`${BASE_URL}/buscar?ods=1`);
  
//   if (!response.ok) {
//     throw new Error(`Erro ao buscar dados iniciais: ${response.statusText}`);
//   }

//   return response.json();
// }
