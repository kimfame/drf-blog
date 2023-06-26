import React from 'react';

import { TailSpin } from 'react-loader-spinner';

const Loading = () => (
  <div className="flex justify-center items-center h-80">
    <TailSpin
      height="100"
      width="100"
      color="#1e40af"
      ariaLabel="tail-spin-loading"
      radius="1"
      wrapperStyle={{}}
      wrapperClass=""
      visible
    />
  </div>
);

export default Loading;
