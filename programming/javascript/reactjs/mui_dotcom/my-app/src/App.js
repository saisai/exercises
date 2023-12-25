import './App.css';


import GlobalCss  from './data/styles/advanced/GlobalCss';
import HybridGlobalCss  from './data/styles/advanced/HybridGlobalCss';

import CustomColor  from './customization/palette/CustomColor';
import ContrastThreshold  from './customization/palette/ContrastThreshold';
import AddingColorTokens  from './customization/palette/AddingColorTokens';
import MediaQuery  from './customization/breakpoints/MediaQuery';
import DefaultProps  from './customization/theme-components/DefaultProps';
import ToggleColorMode  from './customization/dark-mode/ToggleColorMode';
import DarkThemeWithCustomPalette  from './customization/dark-mode/DarkThemeWithCustomPalette';
import DarkTheme  from './customization/dark-mode/DarkTheme';
import CustomStyles  from './customization/theming/CustomStyles';
import ThemeNesting  from './customization/theming/ThemeNesting';
import ThemeNestingExtend  from './customization/theming/ThemeNestingExtend';
import Color  from './customization/color/Color';

function App() {
  return (
    <>
	<br />
	<GlobalCss />
	<br />
	<HybridGlobalCss />
	<br />
	<CustomColor />
	<br />
	<ContrastThreshold />
	<br />
	<AddingColorTokens />
	<br />
	<MediaQuery />
	<br />
	<DefaultProps />
	<br />
	<ToggleColorMode />
	<br />
	<DarkThemeWithCustomPalette />
	<br />
	<DarkTheme />
	<br />
	<CustomStyles />
	<br />
	<br />
	<br />
	<br />
	<br />
	<ThemeNesting />
	<br />
	<ThemeNestingExtend />
	<br />
	<Color />
	</>
  );
}

export default App;
