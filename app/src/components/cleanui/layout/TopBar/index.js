import React, { useState, useEffect } from 'react'
import moment from 'moment'
import { DatePicker, Select } from 'antd'
import Cookies from 'js-cookie'
import _ from 'lodash'
import IssuesHistory from './IssuesHistory'
import UserMenu from './UserMenu'
import style from './style.module.scss'

const { RangePicker } = DatePicker
const { Option } = Select

const TopBar = () => {
  const startDate = Cookies.get('startDate')
  const endDate = Cookies.get('endDate')
  const pickerSession = Cookies.get('picker')
  const [dateFormat, setDateFormat] = useState('YYYY-MM-DD')
  const defaultDateRange =
    startDate && endDate ? [moment(startDate, dateFormat), moment(endDate, dateFormat)] : []
  const [picker, setPicker] = useState(pickerSession || 'date')
  const [values, setValues] = useState(defaultDateRange)

  useEffect(() => {
    if (picker === 'year') {
      setDateFormat('YYYY')
    } else if (picker === 'month') {
      setDateFormat('YYYY-MM')
    } else {
      setDateFormat('YYYY-MM-DD')
    }
  }, [])

  const handleChangeDate = (dates, dateStrings) => {
    Cookies.set('picker', picker)
    let start = dateStrings.shift()
    let end = dateStrings.pop()
    if (!_.isEmpty(start) && !_.isEmpty(end)) {
      if (picker === 'month') {
        start = `${start}-01`
        end = `${end}-01`
      } else if (picker === 'year') {
        start = `${start}-01-01`
        end = `${end}-12-31`
      }
    }
    Cookies.set('startDate', start)
    Cookies.set('endDate', end)
    setValues(dates)
    window.location.reload()
  }

  const handleChangePicker = selectedPicker => {
    if (selectedPicker === 'year') {
      setDateFormat('YYYY')
    } else if (selectedPicker === 'month') {
      setDateFormat('YYYY-MM')
    } else {
      setDateFormat('YYYY-MM-DD')
    }
    setPicker(selectedPicker)
  }

  const disabledDate = current => {
    const start = '2018-01-01'
    const end = '2021-01-07'
    if (current < moment(start)) {
      return true
    }

    return current > moment(end)
  }

  return (
    <div className={style.topbar}>
      <div className="mr-4 d-none d-md-block">
        <IssuesHistory />
      </div>
      <div className="ml-auto">
        <div className="row">
          <div className="col-10">
            <div className="row">
              <div className="col-3">
                <Select defaultValue="date" value={picker} onChange={handleChangePicker}>
                  <Option value="date">Date</Option>
                  <Option value="month">Month</Option>
                  <Option value="year">Year</Option>
                </Select>
              </div>
              <div className="col-9">
                <RangePicker
                  picker={picker}
                  value={values}
                  format={dateFormat}
                  onChange={handleChangeDate}
                  disabledDate={disabledDate}
                />
              </div>
            </div>
          </div>
          <div className="col-2">
            <UserMenu />
          </div>
        </div>
      </div>
    </div>
  )
}

export default TopBar
