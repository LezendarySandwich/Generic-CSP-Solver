import './../styles/outStyles.css'

function OutForm(props){
    return (
        <form className="outStyle">
            <textarea readOnly={true} className="outForm" value={props.value}/>
        </form>
    )
}

export default OutForm