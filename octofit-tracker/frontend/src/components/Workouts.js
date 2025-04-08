import React, { useEffect, useState } from 'react';

function Workouts() {
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        fetch('https://friendly-rotary-phone-8000.app.github.dev/api/workouts/')
            .then(response => response.json())
            .then(data => setWorkouts(data))
            .catch(error => console.error('Error fetching workouts:', error));
    }, []);

    return (
        <div className="container mt-4">
            <h1 className="text-center">Workouts</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Workout Name</th>
                        <th>Difficulty Level</th>
                    </tr>
                </thead>
                <tbody>
                    {workouts.map(workout => (
                        <tr key={workout.id}>
                            <td>{workout.workout_name}</td>
                            <td>{workout.difficulty_level}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Workouts;