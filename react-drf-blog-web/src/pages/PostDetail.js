import { React, useEffect } from 'react';

import DOMPurify from 'dompurify';
import { useQuery } from 'react-query';
import { Link, useNavigate, useParams } from 'react-router-dom';

import Loading from '../components/Loading';
import Utterances from '../components/Utterances';
import fetcher from '../plugins/react-query';

const PostDetail = () => {
  const { postId } = useParams();
  const { data: post, isError, isLoading } = useQuery(`/posts/${postId}`, fetcher);
  const navigate = useNavigate();

  useEffect(() => {
    if (isError) {
      navigate('/404');
    }
  }, [isError, navigate]);

  if (isLoading) {
    return <Loading />;
  }

  return (
    <div className="container mx-auto md:max-w-3xl">
      <div
        className="px-4 md:px-6 text-xl text-gray-800 leading-normal"
        style={{ fontfamily: 'Georgia,serif' }}
      >
        <div className="font-sans">
          <p className="text-base md:text-sm text-blue-800 font-bold">
            &lt;{' '}
            <button
              type="button"
              className="text-base md:text-sm text-blue-800 font-bold no-underline hover:underline"
              onClick={() => navigate('/')}
            >
              BACK TO LIST
            </button>
          </p>
          <h1 className="font-bold font-sans break-normal text-gray-900 pt-6 pb-2 text-3xl md:text-4xl">
            {post?.title}
          </h1>
          <p className="text-sm md:text-base font-normal text-gray-600">
            Published
            {post?.created_at}
          </p>
        </div>

        <div
          className="py-6"
          dangerouslySetInnerHTML={{
            __html: DOMPurify.sanitize(post?.content),
          }}
        />
      </div>

      <div className="flex flex-wrap px-4 py-6">
        {post?.tags?.map((tag) => (
          <span
            key={tag.id}
            className="text-base md:text-sm text-gray-200 bg-blue-800 no-underline px-2 py-0.5 ml-2 rounded-full"
          >
            {tag.name}
          </span>
        ))}
      </div>

      <hr className="border-b-2 border-gray-400 mb-8 mx-4" />
      <div className="container px-4">
        <Utterances />
      </div>
      <hr className="border-b-2 border-gray-400 mb-8 mx-4" />

      <div className="font-sans flex justify-between content-center px-4 pb-12">
        <div className="text-left">
          <span className="text-xs md:text-sm font-normal text-gray-600">&lt; Previous Post</span>
          <br />
          <p>
            <Link
              to={`/post/${post?.previous?.slug}`}
              className="break-normal text-base md:text-sm text-blue-800 font-bold no-underline hover:underline"
            >
              {post?.previous?.title}
            </Link>
          </p>
        </div>
        <div className="text-right">
          <span className="text-xs md:text-sm font-normal text-gray-600">Next Post &gt;</span>
          <br />
          <p>
            <Link
              to={`/post/${post?.next?.slug}`}
              className="break-normal text-base md:text-sm text-blue-800 font-bold no-underline hover:underline"
            >
              {post?.next?.title}
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default PostDetail;
