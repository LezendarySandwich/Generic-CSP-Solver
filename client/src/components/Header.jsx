import {AppBar, Toolbar, Typography, makeStyles} from "@material-ui/core"
import cspImgLogo from './../Images/CSP_solver_logo.png'
import './../styles/logo.css'

const useStyles = makeStyles(() => ({
    logo: {
        fontWeight: 200,
        fontSize: 22,
        color: "white"
    },
    header: {
        backgroundColor: "#252525",
        // borderBottomLeftRadius: "10% 10%",
        // borderBottomRightRadius: "10% 10%",
        alignItems: "center"
    },
}))

function Header(){

    const {header, logo} = useStyles()

    const cspLogo = (
        <Typography variant = "h6" component = "h1" className = {logo}>
            Generic CSP Solver
        </Typography>
    )

    const displayDesktop = () => 
        <Toolbar>
            {cspLogo}
            <img src={cspImgLogo} alt="logo" className="csp-logo-header"/>
        </Toolbar>
    

    return (
        <header>
            <AppBar className = {header}>
                {displayDesktop()}
            </AppBar>
        </header>
    )
}

export default Header