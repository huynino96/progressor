export default async function getMenuData() {
  return [
    {
      category: true,
      title: 'Counter',
    },
    {
      title: 'Class',
      key: 'countClass',
      icon: 'fe fe-home',
      url: '/counter/class',
    },
    {
      title: 'Comment',
      key: 'countComment',
      icon: 'fe fe-database',
      url: '/counter/comment',
    },
    {
      title: 'Library',
      key: 'countLibrary',
      icon: 'fe fe-hard-drive',
      url: '/counter/library',
    },
    {
      title: 'Line Of Code',
      key: 'countLineOfCode',
      icon: 'fe fe-user',
      url: '/counter/line-of-code',
    },
    {
      title: 'Method',
      key: 'countMethod',
      icon: 'fe fe-shopping-cart',
      url: '/counter/method',
    },
    {
      title: 'Testing',
      key: 'countTesting',
      icon: 'fe fe-bookmark',
      url: '/counter/testing',
    },
    {
      title: 'File And Folder',
      key: 'countFileAndFolder',
      icon: 'fe fe-folder',
      url: '/counter/file-and-folder',
    },
  ]
}
