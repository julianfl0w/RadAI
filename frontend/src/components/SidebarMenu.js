import React from 'react';
import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';

const SidebarMenu = () => {
  return (
    <div className="sidebar-wrapper">
    <Sidebar>
      <Menu>
        <MenuItem> Home </MenuItem>
        <MenuItem> Methods </MenuItem>
        <MenuItem> Upload </MenuItem>
        <MenuItem> Contact Us </MenuItem>
      </Menu>
    </Sidebar>
    </div>
  );
};

export default SidebarMenu;
