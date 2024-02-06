import * as React from 'react'
import { makeStyles } from '@mui/styles'
import HoverMenu from 'material-ui-popup-state/HoverMenu'
import MenuItem from '@mui/material/MenuItem'
import ChevronRight from '@mui/icons-material/ChevronRight'
import Button from '@mui/material/Button'
import Link from '@mui/material/Link';
import { Link as RLink, Outlet  } from "react-router-dom";
import {
  usePopupState,
  bindHover,
  bindFocus,
  bindMenu,
} from 'material-ui-popup-state/hooks'

const useCascadingMenuStyles = makeStyles((theme) => ({
  submenu: {
    marginTop: theme.spacing(-1),
  },
  title: {
    flexGrow: 1,
  },
  moreArrow: {
    marginRight: theme.spacing(-1),
  },
}))

const CascadingContext = React.createContext({
  parentPopupState: null,
  rootPopupState: null,
})

function CascadingMenuItem({ onClick, ...props }) {
  const { rootPopupState } = React.useContext(CascadingContext)
  if (!rootPopupState) throw new Error('must be used inside a CascadingMenu')
  const handleClick = React.useCallback(
    (event) => {
      rootPopupState.close(event)
      if (onClick) onClick(event)
    },
    [rootPopupState, onClick]
  )

  return <MenuItem {...props} onClick={handleClick} />
}

function CascadingSubmenu({ title, popupId, ...props }) {
  const classes = useCascadingMenuStyles()
  const { parentPopupState } = React.useContext(CascadingContext)
  const popupState = usePopupState({
    popupId,
    variant: 'popover',
    parentPopupState,
  })
  return (
    <React.Fragment>
      <MenuItem {...bindHover(popupState)} {...bindFocus(popupState)}>
        <span className={classes.title}>{title}</span>
        <ChevronRight className={classes.moreArrow} />
      </MenuItem>
      <CascadingMenu
        {...props}
        classes={{ ...props.classes, paper: classes.submenu }}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        transformOrigin={{ vertical: 'top', horizontal: 'left' }}
        popupState={popupState}
      />
    </React.Fragment>
  )
}

function CascadingMenu({ popupState, ...props }) {
  const { rootPopupState } = React.useContext(CascadingContext)
  const context = React.useMemo(
    () => ({
      rootPopupState: rootPopupState || popupState,
      parentPopupState: popupState,
    }),
    [rootPopupState, popupState]
  )

  return (
    <CascadingContext.Provider value={context}>
      <HoverMenu {...props} {...bindMenu(popupState)} />
    </CascadingContext.Provider>
  )
}

const CascadingHoverMenus = () => {
  const popupState = usePopupState({
    popupId: 'demoMenu',
    variant: 'popover',
  })
  return (
    <div>
      {/* <Button
        variant="contained"
        {...bindHover(popupState)}
        {...bindFocus(popupState)}
      >
        Settings
      </Button> */}
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
      <Link variant="button" 
        {...bindHover(popupState)}
        {...bindFocus(popupState)}>
        Settings
      </Link>
      <CascadingMenu
        popupState={popupState}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'left' }}
        transformOrigin={{ vertical: 'top', horizontal: 'left' }}
      >
        <CascadingMenuItem>
            <RLink to="/applytest">Email</RLink>
        </CascadingMenuItem>
        <CascadingMenuItem>
            <RLink to="/applytest">Line App</RLink>
        </CascadingMenuItem>
        <CascadingSubmenu
          popupId="moreChoicesCascadingMenu"
          title="More Choices"
        >
          <CascadingMenuItem>Cheesecake</CascadingMenuItem>
          <CascadingMenuItem>Cheesedeath</CascadingMenuItem>
          <CascadingSubmenu
            popupId="evenMoreChoicesCascadingMenu"
            title="Even More Choices"
          >
            <CascadingMenuItem>Cake (the band)</CascadingMenuItem>
            <CascadingMenuItem>Death Metal</CascadingMenuItem>
          </CascadingSubmenu>
          <CascadingSubmenu
            popupId="moreBenignChoices"
            title="More Benign Choices"
          >
            <CascadingMenuItem>Salad</CascadingMenuItem>
            <CascadingMenuItem>Lobotomy</CascadingMenuItem>
          </CascadingSubmenu>
        </CascadingSubmenu>
      </CascadingMenu>

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
        to="/jobsdb/"
    >
        JobsDb
    </Link>
      

    </div>
  )
}

export default CascadingHoverMenus