import React from 'react'
import { Menu, Dropdown } from 'antd'
import Cookies from 'js-cookie'
import { REPOSITORY_ENDPOINT } from 'utils/constants'
import styles from './style.module.scss'

const IssuesHistory = () => {

  const handleClick = repositoryEndpoint => {
    document.cookie = `repositoryEndpoint=${repositoryEndpoint}`;
    window.location.reload();
  }

  const menu = (
    <Menu selectable={false}>
      <Menu.ItemGroup title="Java">
        <Menu.Item onClick={() => handleClick('kagkarlsson/db-scheduler')}>
          kagkarlsson/db-scheduler
        </Menu.Item>
      </Menu.ItemGroup>
      <Menu.Divider />
      <Menu.ItemGroup title="Javascript">
        <Menu.Item onClick={() => handleClick('axios/axios')}>
          axios/axios
        </Menu.Item>
      </Menu.ItemGroup>
      <Menu.Divider />
      <Menu.ItemGroup title="Python">
        <Menu.Item onClick={() => handleClick('Pylons/deform')}>
          Pylons/deform
        </Menu.Item>
      </Menu.ItemGroup>
      <Menu.Divider />
      <Menu.ItemGroup title="PHP">
        <Menu.Item onClick={() => handleClick('sebastianbergmann/php-timer')}>
          sebastianbergmann/php-timer
        </Menu.Item>
      </Menu.ItemGroup>
    </Menu>
  )
  return (
    <Dropdown overlay={menu} trigger={['click']} placement="bottomLeft">
      <div className={styles.dropdown}>
        <i className={`${styles.icon} fe fe-folder`} />
        <span className="d-none d-xl-inline">
          {Cookies.get('repositoryEndpoint') || REPOSITORY_ENDPOINT}
        </span>
      </div>
    </Dropdown>
  )
}

export default IssuesHistory
