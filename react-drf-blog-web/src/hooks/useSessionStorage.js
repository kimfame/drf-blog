import { useEffect, useState } from 'react';

const useSessionStorage = (key, initialValue) => {
  const [value, setValue] = useState(initialValue);

  useEffect(() => {
    const item = window.sessionStorage.getItem(key);
    if (item) {
      setValue(JSON.parse(item));
    }
  }, []);

  const setFunction = (newValue) => {
    window.sessionStorage.setItem(key, JSON.stringify(newValue));
    setValue(newValue);
  };

  return [value, setFunction];
};

export default useSessionStorage;
