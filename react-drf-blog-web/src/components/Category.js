import React from 'react';

import PropTypes from 'prop-types';

const Category = ({ on, toggle, name }) => (
  <button
    type="button"
    className={`border py-1 px-2 mx-3 my-2 rounded-full cursor-pointer
        ${on ? 'bg-blue-200 hover:bg-blue-200' : 'hover:bg-gray-200'}`}
    onClick={toggle}
  >
    {name}
  </button>
);

Category.propTypes = {
  on: PropTypes.bool.isRequired,
  toggle: PropTypes.func.isRequired,
  name: PropTypes.string.isRequired,
};

export default Category;
