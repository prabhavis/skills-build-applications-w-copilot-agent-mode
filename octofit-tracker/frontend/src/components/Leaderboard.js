import React, { useEffect, useState } from 'react';

function Leaderboard() {
    const [leaderboard, setLeaderboard] = useState([]);

    useEffect(() => {
        fetch('https://friendly-rotary-phone-8000.app.github.dev/api/leaderboard/')
            .then(response => response.json())
            .then(data => setLeaderboard(data))
            .catch(error => console.error('Error fetching leaderboard:', error));
    }, []);

    return (
        <div className="container mt-4">
            <h1 className="text-center">Leaderboard</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Team Name</th>
                        <th>Total Points</th>
                    </tr>
                </thead>
                <tbody>
                    {leaderboard.map(entry => (
                        <tr key={entry.id}>
                            <td>{entry.team_name}</td>
                            <td>{entry.total_points}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Leaderboard;