import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useState, useEffect} from 'react';

function App() {

  const [body, setBody] = useState('')

  useEffect(
    () => {
      axios
        .get("http://localhost:8000/get_data")
        .then((response) => {
          const data = response.data
          setBody(data['message'])
        })
    }, [])

  return (
    <div>
      {body}
    </div>
  );
}

export default App;
