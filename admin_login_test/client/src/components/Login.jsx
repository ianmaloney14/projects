import axios from 'axios'

const Login = (props) => {
    return (
        <div>
            <form>
                <label>username:</label>
                <input type="text" />
                <label>password:</label>
                <input type="text" />
                <div>
                    <button>Login</button>
                </div>
            </form>
        </div>
    )
}

export default Login;