import api from './axios';

async function fetcher({ queryKey }) {
  try {
    const response = await api.get(queryKey[0]);
    return response.data;
  } catch (error) {
    if (error?.response?.status === 404) {
      throw new Error('Page Not Found');
    } else {
      throw new Error(error?.message);
    }
  }
}

export default fetcher;
