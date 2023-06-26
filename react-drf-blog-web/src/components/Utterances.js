import { React, useEffect, useRef } from 'react';

const Utterances = () => {
  const comments = useRef(null);

  useEffect(() => {
    if (comments.current.children[0]) {
      return;
    }
    const scriptElement = document.createElement('script');
    scriptElement.async = true;
    scriptElement.src = 'https://utteranc.es/client.js';
    scriptElement.setAttribute('repo', process.env.REACT_APP_UTTERANCES_COMMENT_GITHUB_URL);
    scriptElement.setAttribute('issue-term', 'pathname');
    scriptElement.setAttribute('label', 'utterances');
    scriptElement.setAttribute('theme', 'github-light');
    scriptElement.setAttribute('crossorigin', 'anonymous');
    comments.current?.appendChild(scriptElement);
  }, []);

  return <div ref={comments} />;
};

export default Utterances;
