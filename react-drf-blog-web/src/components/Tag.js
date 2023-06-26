import React from 'react';

import PropTypes from 'prop-types';

const Tag = ({ on, toggle, name }) => (
  <button
    type="button"
    className={`border px-2 py-0.5 mx-1 my-1 rounded-full cursor-pointer
      ${on ? 'bg-blue-200 hover:bg-blue-200' : 'hover:bg-gray-200'}`}
    onClick={toggle}
  >
    {name}
  </button>
);

Tag.propTypes = {
  on: PropTypes.bool.isRequired,
  toggle: PropTypes.func.isRequired,
  name: PropTypes.string.isRequired,
};

export default Tag;
