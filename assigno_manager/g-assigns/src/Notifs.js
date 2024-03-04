import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Notifs() {
    const [grades, setGrades] = useState(null);

    useEffect(() => {
        (async () => {
            try{
                const url = 'http://localhost:8000/grades/'
                const data = await axios.get(url);
                setGrades(data.data);
                console.log(data.data) // validate data
            } catch (err) {
                console.error(err);
            }
        })();
    }, []);

    return (
       <div>
       <div className="grades">
                {grades && (
                    <ul>
                        {grades.map((grade) => (
                            <li key={grade.title}>{grade.title}: {grade.grade} / {grade.maxPoints}</li> // Assuming each grade has an 'id' property
                        ))}
                    </ul>
                )}
            </div>
       </div>
    )
}

export default Notifs