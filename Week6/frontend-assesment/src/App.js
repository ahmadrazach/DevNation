import './App.css';
import axios from "axios";
//using useEffect
import {useEffect,useState,useReducer} from "react"

const App=()=> {
  //checking if data's fetched
  const [isLoading, setIsLoading] = useState(false);
  //Add Data
  const [data, setData] = useState([]);

  //calling the function using useEffect
  useEffect(()=>{

    axios.get("https://api.hatchways.io/assessment/students")
          .then((res) => {
            console.log(res.data.students)
            setData(res.data.students)
            //console.log(setData)
          })
          .catch((error) => {
            setIsLoading(false);
            console.log(error);
          });
  },[]);

  //finding average
  //first finding sum
  var sum = function(array) {
    var total = 0;
    for (var i=0; i<array.length; i++) {
      total += array[i];
    }
    return total;
  };
  //then average
  var mean = function(array) {
    var arraySum = sum(array);
    return arraySum / array.length;
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (


    <div className="App">
     <div className='main-div'>
        <input
          type="text"
          name="PName"
          id="PName"
          autoComplete="off"
          //value={ProductData.PNAME}
          //onChange={handleInputs}
          placeholder='Search by name'
        />
        {data && data.map((item, index) =>
        <div className='profile-card'>
          <div className='flex-col-img'>
            <img src={item.pic} alt='img'></img>
          </div>
          < div className='flex-col-content'>
            <h2 key={index}>{item.firstName} {item.lastName} </h2>
            <p className='email-p'>Email : {item.email}</p>
            <p>Company : {item.company}</p>
            <p>Skill : {mean(item.grades)}</p>
            <p>Average : {item.skill}</p>
          </div>
        </div>
        )}
    </div>
    </div>
  );
}

export default App;
