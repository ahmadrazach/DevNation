import './App.css';
import axios from "axios";
//using useEffect
import {useEffect,useState,useReducer} from "react"

const App=()=> {
  //checking if data's fetched
  const [isLoading, setIsLoading] = useState(false);
  //Add Data
  const [data, setData] = useState([]);
    //taking the search Term
    const [searchTerm,setSearchTerm]=useState('')
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
  var mean = function(array) {
    const avg=array.grades.reduce((sum, curr) => sum + Number(curr), 0) /array.grades.length;
    return avg;
    
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  //clicking functionality
  var changeButton=function()
  {
    var acc = document.getElementsByClassName("accordion");
  var i;
  
 

  
  for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      //console.log("chalo idhr",acc[i])
      //displayblock.className="display"
       //displayblock.className="display"
       var displayblock=document.getElementById("nodisplay");
        var currentId = displayblock.id;
        if (currentId == "display") { // Check the current class name
          displayblock.id = "nodisplay";   // Set other class name
        }
        else if(currentId == "nodisplay"){
        displayblock.id = "display";  
        }
        else {
            displayblock.id = "display";  // Otherwise, use `second_name`
        }
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        //document.getElementById("display").id='nodisplay';
      } else 
      {
        //document.getElementById("nodisplay").id='display';
        panel.style.maxHeight = panel.scrollHeight + "px";
      } 

    });
  }
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
          onChange={e=>setSearchTerm(e.target.value)}
          placeholder='Search by name'
        />
        {data && data
        //checking if product name matches
        .filter((product)=>{
          if(searchTerm=="")
          {
            return product
          }
          else if(product.firstName.toLowerCase().includes(searchTerm.toLowerCase()) || product.lastName.toLowerCase().includes(searchTerm.toLowerCase())){
            return product
          }
        })
        //map function
        .map((item, index) =>
        <div className='profile-card'>
          <div className='flex-col-img'>
            <img src={item.pic} alt='img'></img>
          </div>
          < div className='flex-col-content'>
            <h2 key={index}>{item.firstName} {item.lastName} </h2>
            <p className='email-p'>Email : {item.email}</p>
            <p>Company : {item.company}</p>
            <p>Skill : {mean(item)}</p>
            <p>Average : {item.skill}</p>
            <div className='grade ' id="nodisplay">
              <p>Test 1 : {item.grades[index]}</p>
              <p>Test 2 : {item.grades[index+1]}</p>
              <p>Test 3 : {item.grades[index+2]}</p>
              <p>Test 4 : {item.grades[index+3]}</p>
              <p>Test 5 : {item.grades[index+4]}</p>
              <p>Test 6 : {item.grades[index+5]}</p>
              <p>Test 7 : {item.grades[index+6]}</p>
              <p>Test 8 : {item.grades[index+7]}</p>
            </div>

          </div>
          <button class="accordion" onClick={changeButton}></button>
        </div>
        )}
    </div>

    </div>
  );
}

export default App;
