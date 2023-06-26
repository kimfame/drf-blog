import { React, useEffect, useRef } from 'react';

const Header = () => {
  const targetRef = useRef(null);

  const handleScroll = () => {
    const h = document.documentElement;
    const b = document.body;
    const st = 'scrollTop';
    const sh = 'scrollHeight';
    const progress = targetRef.current;

    const scroll = ((h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight)) * 100;
    progress.style.setProperty('--scroll', `${scroll}%`);
  };

  useEffect(() => {
    document.addEventListener('scroll', handleScroll);

    document.getElementById('nav-toggle').onclick = () => {
      document.getElementById('nav-content').classList.toggle('hidden');
    };
  }, []);

  return (
    <header>
      <nav ref={targetRef} className="fixed w-full bg-blue-800 z-10 top-0 pb-2">
        <div
          id="progress"
          className="h-1 z-20 top-0"
          style={{
            background: 'linear-gradient(to right, #93C5FD var(--scroll), transparent 0)',
          }}
        />
        <div className="w-full md:max-w-4xl mx-auto flex flex-wrap items-center justify-between mt-0 py-3">
          <div className="pl-4">
            <a className="text-gray-200 text-xl font-extrabold no-underline" href="/">
              Tech Blog
            </a>
          </div>

          <div className="block lg:hidden pr-4">
            <button
              type="button"
              id="nav-toggle"
              className="flex items-center px-3 py-2 border rounded text-gray-400 border-gray-400 hover:text-gray-200 hover:border-gray-200 appearance-none focus:outline-none"
            >
              <svg
                className="fill-current h-3 w-3"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <title>Menu</title>
                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
              </svg>
            </button>
          </div>

          <div
            className="w-full flex-grow lg:items-center lg:w-auto hidden lg:block mt-2 lg:mt-0 bg-blue-800 md:bg-transparent z-20"
            id="nav-content"
          >
            <ul className="list-reset lg:flex justify-end flex-1 items-center">
              <li className="mr-3">
                <a
                  className="inline-block py-2 px-4 no-underline text-gray-300 hover:text-gray-100 hover:font-bold"
                  href="/"
                >
                  Post
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
