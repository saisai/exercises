import BoxSx from "./layout/box/BoxSx";
import NestedGrid from "./layout/grid/NestedGrid";
import BasicGrid from "./layout/grid2/BasicGrid";
import FullWidthGrid from "./layout/grid2/FullWidthGrid";

export default function LayoutMain() {
    return(
        <>
        <BoxSx />
        <NestedGrid />
        <BasicGrid />
        <FullWidthGrid />
        </>
    );
}