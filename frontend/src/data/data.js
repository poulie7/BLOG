// const axios = require('axios').default;
import axios from 'axios';
// const articles = ref([]);
export function DataService(){
  const getPosts = async () => {
    try {
        const response = await axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api'
        });
        console.log(response.data)
        return response.data; // Return the fetched articles
    } catch (error) {
      
        console.error('Error fetching articles:', error);
        return []; // Return an empty array in case of error
    }
};
  return {
    getPosts,
  };
}

// function main() {
//   const response =  axios({
//       method: 'GET',
//       url: 'http://127.0.0.1:8000/api'
//   })
// .then(response => {
//   const jsonData = response.data;
//   console.log(jsonData)
// })
// }

// main()
