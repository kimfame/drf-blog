import React from 'react';

import { Navigate, Route, Routes } from 'react-router-dom';

import RouteChangeTracker from './components/RouteChangeTracker';
import Index from './pages/Index';
import NotFound from './pages/NotFound';
import PostDetail from './pages/PostDetail';

function App() {
  if (process.env.REACT_APP_GOOGLE_ANALYTICS_TRACKING_ID) {
    RouteChangeTracker();
  }

  return (
    <Routes>
      <Route path="/" element={<Index />} />
      <Route path="/post/:postId" element={<PostDetail />} />
      <Route path="/404" element={<NotFound />} />
      <Route path="/*" element={<Navigate to="/404" replace />} />
    </Routes>
  );
}

export default App;
