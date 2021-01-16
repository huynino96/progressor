import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import Cookies from 'js-cookie'
import { REPOSITORY_ENDPOINT } from 'utils/constants'
import client from 'client'
import capitalize from 'capitalize'
import _ from 'lodash'

import CountChart from '../../components/CountChart'

/* eslint-disable */
const Counter = () => {
  const [data, setData] = useState([])
  const { language } = useParams()

  useEffect(() => {
    fetchData()
  }, [])

  const getKeyword = () => {
    return language.replace(/-/g, '_').replace('ing', '')
  }

  const getFormatDate = date => {
    const picker = Cookies.get('picker')
    if (picker === 'month') {
      const dates = date.split('-')
      dates.pop()
      return dates.join('-')
    } else if (picker === 'year') {
      const dates = date.split('-')
      dates.pop()
      dates.pop()
      return dates.join('-')
    }
    return date
  }

  const fetchData = async () => {
    const repositoryEndpoint = Cookies.get('repositoryEndpoint')
    const startDate = Cookies.get('startDate')
    const endDate = Cookies.get('endDate')
    const keyword = getKeyword()
    const finalRepositoryEndpoint = repositoryEndpoint || REPOSITORY_ENDPOINT
    const query = { repository: finalRepositoryEndpoint }
    if (startDate && endDate) {
      query.start_date = startDate
      query.end_date = endDate
    }
    const response = await client.get(`/language/${keyword}`, { params: query })
    const results =
      keyword === 'file_and_folder'
        ? response.data.map(item => ({
            name: getFormatDate(item.date),
            file: item.file,
            folder: item.folder,
          }))
        : response.data.map(item => ({
            name: getFormatDate(item.date),
            total: item.total,
            javascript: item.javascript,
            java: item.java,
            python: item.python,
            php: item.php,
          }))
    console.log(results)
    const finalResult = _.chain(results)
      .groupBy('name')
      .map((value, key) => ({
        name: key,
        file: _.sumBy(value, 'file'),
        folder: _.sumBy(value, 'folder'),
        total: _.sumBy(value, 'total'),
        javascript: _.sumBy(value, 'javascript'),
        java: _.sumBy(value, 'java'),
        python: _.sumBy(value, 'python'),
        php: _.sumBy(value, 'php'),
      }))
      .value()

    setData(finalResult)
  }

  const title = capitalize.words(language.split('-').join(' '))
  const keyword = getKeyword()
  return <CountChart title={title} data={data} keyword={keyword} />
}

export default Counter
