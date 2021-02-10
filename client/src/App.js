import Header from "./components/Header"
import Forms from "./components/Forms"
import Footer from "./components/Footer"
import "./styles/App.css"

function App() {
  return (
    <div className="page-container">
      <div className="content-wrap">
        <Header />
        <Forms /> 
      </div>
      <Footer />
    </div>
  )
}

export default App
