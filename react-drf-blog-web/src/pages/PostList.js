import { React, useState } from 'react';

import PropTypes from 'prop-types';
import { useQuery } from 'react-query';
import { Link } from 'react-router-dom';

import Loading from '../components/Loading';
import fetcher from '../plugins/react-query';

const PostList = ({ categories, tags }) => {
  const [pageNum, setPageNum] = useState(1);
  const { data, isLoading } = useQuery(
    `/posts/?page=${pageNum}${categories.length > 0 ? `&categories=${categories.toString()}` : ''}${
      tags.length > 0 ? `&tags=${tags.toString()}` : ''
    }`,
    fetcher,
  );

  const moveNextPage = () => {
    if (data?.next) {
      setPageNum((prePageNum) => {
        const newPrePageNum = prePageNum + 1;
        return newPrePageNum;
      });
    }
  };

  const movePreviousPage = () => {
    if (data?.previous) {
      setPageNum((prePageNum) => {
        const newPrePageNum = prePageNum - 1;
        return newPrePageNum;
      });
    }
  };

  if (isLoading) {
    return <Loading />;
  }

  return (
    <>
      {data?.results?.map((post) => (
        <article key={post.slug} className="flex flex-col shadow my-4 w-full">
          <div className="flex flex-col bg-white justify-start p-6">
            <div className="flex flex-wrap">
              {post.categories.map((category) => (
                <span
                  key={category.id}
                  className="text-blue-700 text-sm font-bold uppercase pr-5 pb-4"
                >
                  {category.name}
                </span>
              ))}
            </div>
            <Link to={`/post/${post.slug}`} className="text-3xl font-bold hover:text-gray-400 pb-4">
              {post.title}
            </Link>
            <p className="text-sm pb-3">
              Published on
              {post.created_at}
            </p>
            <p className="pb-6">{post.summary}</p>
            <Link to={`/post/${post.slug}`} className="text-gray-800 hover:text-black">
              Continue Reading ...
              <i className="fas fa-arrow-right" />
            </Link>
          </div>
        </article>
      ))}

      {data && (
        <div className="flex items-center py-8">
          <button
            type="button"
            className={`${
              data?.previous
                ? 'hover:bg-blue-600 hover:text-white'
                : 'bg-gray-200 hover:bg-gray-200'
            } h-10 w-10 font-semibold text-gray-800 text-sm flex items-center justify-center`}
            onClick={() => movePreviousPage()}
          >
            {'<'}
          </button>
          <button
            type="button"
            className={`${
              data?.next ? 'hover:bg-blue-600 hover:text-white' : 'bg-gray-200 hover:bg-gray-200'
            } h-10 w-10 font-semibold text-gray-800 text-sm flex items-center justify-center`}
            onClick={() => moveNextPage()}
          >
            {'>'}
          </button>
        </div>
      )}
    </>
  );
};

PostList.defaultProps = {
  categories: [],
  tags: [],
};

PostList.propTypes = {
  categories: PropTypes.arrayOf(PropTypes.number),
  tags: PropTypes.arrayOf(PropTypes.number),
};

export default PostList;
