import { React, useState } from 'react';

import { useQuery } from 'react-query';

import PostList from './PostList';
import Category from '../components/Category';
import Tag from '../components/Tag';
import useSessionStorage from '../hooks/useSessionStorage';
import fetcher from '../plugins/react-query';

const Index = () => {
  const [categories, setCategories] = useSessionStorage('categories', []);
  const [tags, setTags] = useSessionStorage('tags', []);
  const [TagFetchSwitch, setTagFetchSwitch] = useState(false);
  const [pageNum, setPageNum] = useSessionStorage('pageNum', 1);

  function getSelectedCategories() {
    return categories.filter((category) => category.on === true).map((category) => category.id);
  }

  function getSelectedTags() {
    return tags.filter((tag) => tag.on === true).map((tag) => tag.id);
  }

  useQuery('/categories/', fetcher, {
    onSuccess: (data) => {
      setCategories(data.map((category) => ({ ...category, on: false })));
      setTagFetchSwitch(true);
      setPageNum(1);
    },
    enabled: !categories.length,
    staleTime: Infinity,
    cacheTime: Infinity,
  });

  useQuery(
    getSelectedCategories().length > 0 ? `/tags/?categories=${getSelectedCategories()}` : '/tags/',
    fetcher,
    {
      onSuccess: (data) => {
        setTagFetchSwitch(false);
        setTags(data.map((tag) => ({ ...tag, on: false })));
      },
      enabled: TagFetchSwitch,
      cacheTime: Infinity,
    },
  );

  const toggleCategory = (id) => {
    setTagFetchSwitch(true);
    setPageNum(1);
    setCategories(
      categories.map((category) =>
        category.id === id ? { ...category, on: !category.on } : category,
      ),
    );
  };

  const toggleTag = (id) => {
    setTagFetchSwitch(false);
    setPageNum(1);
    setTags(tags.map((tag) => (tag.id === id ? { ...tag, on: !tag.on } : tag)));
  };

  return (
    <>
      <div className="container mx-auto">
        <div className="flex flex-col items-center py-12">
          <a className="font-bold text-gray-800 uppercase hover:text-gray-700 text-5xl" href="/">
            Tech Blog
          </a>
          <p className="text-lg text-gray-600">Welcome to Tech Info World!</p>
        </div>
      </div>

      <nav className="w-full py-4 border-t border-b bg-gray-100">
        <div className="w-full md:max-w-4xl container mx-auto">
          <div className="flex flex-wrap items-center justify-center text-sm uppercase mt-0 px-6 py-2">
            {categories.map((category) => (
              <Category
                key={category.id}
                toggle={() => toggleCategory(category.id)}
                name={category.name}
                on={category.on}
              />
            ))}
          </div>
        </div>
      </nav>

      <div className="container mx-auto flex flex-wrap py-6">
        <section className="w-full md:w-2/3 flex flex-col items-center px-3">
          <PostList
            categories={getSelectedCategories()}
            tags={getSelectedTags()}
            pageNum={pageNum}
            setPageNum={setPageNum}
          />
        </section>

        <aside className="w-full md:w-1/3 flex flex-col items-center px-3">
          <div className="w-full bg-white shadow flex flex-col my-4 p-6">
            <p className="text-xl font-semibold pb-5">Tags</p>
            <div className="flex flex-wrap">
              {tags?.map((tag) => (
                <Tag key={tag.id} toggle={() => toggleTag(tag.id)} name={tag.name} on={tag.on} />
              ))}
            </div>
          </div>
        </aside>
      </div>
    </>
  );
};

export default Index;
