import { withFormik, Field, Form } from 'formik'
import OutForm from './OutForm'
import * as Yup from 'yup'
import ReactLoading from 'react-loading'
import './../styles/formStyles.css'

function TemplateForms({values, touched, isSubmitting, errors}){
    const constraintTextHolder = "Constraints \ne.g.\nvalue[1] == value[2]\nvalue[2] + value[3] == 4"
    const constraintPythonHolder = `Constraints \ne.g.\nconstraint = ""\n for i in range(5):\n    constraint += f'value[i] != 1;'\nreturn constraint`
    const domainTextHolder = "Domain\ne.g.\ndomain[1] = [1,2,3]\ndomain[2] = [2,4,1]"
    const domainPythonHolder = `Domain\ne.g.\ndomains = ""\nfor i in range(3):\n    domains += f'domain[{i + 1}] = [1,2,3];'\nreturn domains`

    return (
        <div className="my-container">
            <OutForm value={values.outState}/>
            {<ReactLoading type={"bars"} className={`centerAnimation ${!isSubmitting && "hide"}`} color="#252525"/> }
            <Form className="formStyle">
                <Field component="select" name="algorithm" className="dropDown" style={{width: "25%"}}>
                    <option value="solve_dfs" className="dropDownContent">Depth First Search</option>
                    <option value="solve_BackTrack" className="dropDownContent">Backtracking</option>
                    <option value="solve_ForwardChecking" className="dropDownContent">Forward Checking</option>
                    <option value="solve_ForwardChecking_MRV" className="dropDownContent">Forward Checking (ordering: MRV)</option>
                    <option value="solve_ForwardChecking_MRV_LCV" className="dropDownContent">Forward Checking (ordering: MRV&LCV)</option>
                    <option value="solve_HillClimbing_chooseBest" className="dropDownContent">Classical Hill Climbing</option>
                    <option value="solve_HillClimbing_chooseRandom" className="dropDownContent">Hill Climbing (nighbour: random)</option>
                    <option value="solve_HillClimbing_greedyBias" className="dropDownContent">Hill Climbing (neighbour: biased greedily)</option>
                    <option value="solve_local_beam_search" className="dropDownContent">Local beam search</option>
                    <option value="solve_GeneticAlgo" className="dropDownContent">Genetic Algorithm</option>
                    <option value="solve_Simulated_Annealing" className="dropDownContent">Simulated Annealing</option>
                    <option value="solve_ArcConsistent_BackTracking" className="dropDownContent">Arc consistent backtracking</option>
                    <option value="solve_novelAlgorithm" className="dropDownContent">Hill Climbing with Forward checking</option>
                </Field>
                <Field component="select" name="format" className="dropDown" style={{width: "15%"}}>
                    <option value="text">Text</option>
                    <option value="python">Python</option>
                </Field>
                <Field name="variables" placeholder="Variables" className="variable"/>
                {touched.variables && errors.variables && <h6 className="error">{errors.variables}</h6>}
                <Field component="textarea" spellCheck="false" name="domain" placeholder={values.format === 'text'? domainTextHolder: domainPythonHolder} className="domain"/>
                <Field component="textarea" spellCheck="false" name="constraints" placeholder={values.format === 'text'? constraintTextHolder: constraintPythonHolder} className="constraint"></Field>
                <button disabled={isSubmitting} type = "submit" className="btn" style={{width:"20%"}}>Run</button>
            </Form>
        </div>
        
    )
}

const Forms = withFormik({
    mapPropsToValues(){
        return {
            variables: '',
            domain:'',
            constraints: '',
            algorithm: 'solve_dfs',
            format: 'text',
            outState: '',
        }
    },
    validationSchema: Yup.object().shape({
        variables: Yup.string().matches(/^\d+$/, '*Must be an integer').required('*Required'),
        constraints: Yup.string(),
    }),
    async handleSubmit(values, {setSubmitting, setFieldValue}){
        setSubmitting(true)
        let response = await fetch(`https://csp-server-flask.herokuapp.com/api/${values.variables}/${values.algorithm}/${values.format}/?constraint=${encodeURIComponent(values.constraints)}&domain=${encodeURIComponent(values.domain)}`)
        if(response.ok){
            response = await response.json()
            if(response['timed_out']){
                setFieldValue('outState', 'Timed out...')
            }
            else if(!response['done']){
                setFieldValue('outState', 'No solution exists...')
            }
            else {
                setFieldValue('outState', response['solution'])
            }
        }
        else {
            response = await response.json()
            setFieldValue('outState', response['message'])
        }
        setSubmitting(false)
    }
})(TemplateForms)

export default Forms