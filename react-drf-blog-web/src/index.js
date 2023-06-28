import React from 'react';

import ReactDOM from 'react-dom/client';
import ReactGA from 'react-ga4';
import { QueryClient, QueryClientProvider } from 'react-query';
import { BrowserRouter } from 'react-router-dom';

import './index.css';
import App from './App';
import Layout from './layouts/Layout';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

const TRACKING_ID = process.env.REACT_APP_GOOGLE_ANALYTICS_TRACKING_ID;
ReactGA.initialize(TRACKING_ID);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <Layout>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </Layout>
    </QueryClientProvider>
  </React.StrictMode>,
);
