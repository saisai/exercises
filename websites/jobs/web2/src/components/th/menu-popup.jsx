import * as React from 'react'
import Button from '@mui/material/Button'
import Menu from '@mui/material/Menu'
import MenuItem from '@mui/material/MenuItem'
import Link from '@mui/material/Link';

import { Link as RLink, Outlet  } from "react-router-dom";
import {
  usePopupState,
  bindTrigger,
  bindMenu,
} from 'material-ui-popup-state/hooks'

const MenuPopupState = () => {
  const popupState = usePopupState({ variant: 'popover', popupId: 'demoMenu' })
  return (
    <div>
      <Link
          variant='button'
          color="text.primary"
          href="#"
          sx={{ my: 1, mx: 1.5 }}
          component={RLink}
          to="/applytest"
      >
          Apply Test
      </Link>  

      <Link variant="button" {...bindTrigger(popupState)}>
        Settings
      </Link>
      <Menu {...bindMenu(popupState)}>
        <MenuItem onClick={popupState.close}>        
            <RLink to="/applytest">Email</RLink>
        </MenuItem>
        <MenuItem onClick={popupState.close}>
        <RLink to="/applytest">Line App</RLink>
        </MenuItem>
      </Menu>

      <Link
        variant='button'
        color="text.primary"
        href="#"
        sx={{ my: 1, mx: 1.5 }}
        component={RLink}
        to="/file"
        >
        File
    </Link>  
    <Link
        variant='button'
        color="text.primary"
        href="#"
        sx={{ my: 1, mx: 1.5 }}
        component={RLink}
        to="/position"
    >
        Position
    </Link>  
    <Link
        variant='button'
        color="text.primary"
        href="#"
        sx={{ my: 1, mx: 1.5 }}
        component={RLink}
        to="/apply"
    >
        Apply
    </Link>                      
    <Link
        variant='button'
        color="text.primary"
        href="#"
        sx={{ my: 1, mx: 1.5 }}
        component={RLink}
        to="/jobthai"
    >
        JobThai
    </Link>                
    <Link
        variant='button'
        color="text.primary"
        href="#"
        sx={{ my: 1, mx: 1.5 }}
        component={RLink}
        to="/jobsdb"
    >
        JobsDb
    </Link>
    </div>
  )
}

export default MenuPopupState;