import {AppBar} from '@material-ui/core'
import {SocialIcon} from 'react-social-icons'
import './../styles/footer.css'
import cspImgLogo from './../Images/CSP_solver_logo.png'
import './../styles/logo.css'

export default function Footer() {
    return (
        <AppBar style = {{background: "#252525"}} position="static" color="primary">
            <div className="footerStyle">
                <img src={cspImgLogo} alt="logo" className="csp-logo-footer logo"/>
                {/* <h4 className="logo">Generic CSP Solver</h4> */}
                <SocialIcon className="mailto" url="mailto:mani.1@iitj.ac.in" />
                <SocialIcon className="linkdin-sanskar" url="http://linkedin.com/in/sanskar-mani-5a8431174/?originalSubdomain=in" />
                <SocialIcon className="linkdin-dhruv"url="https://github.com/LezendarySandwich/Generic-CSP-Solver" /> 
        </div>
        </AppBar>
    )
}