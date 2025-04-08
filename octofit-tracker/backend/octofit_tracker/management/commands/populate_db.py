from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(name='John Doe', email='john.doe@example.com', password='password123', age=25, gender='Male'),
            User(name='Jane Smith', email='jane.smith@example.com', password='password123', age=30, gender='Female'),
            User(name='Alice Johnson', email='alice.johnson@example.com', password='password123', age=22, gender='Female'),
            User(name='Bob Brown', email='bob.brown@example.com', password='password123', age=28, gender='Male'),
            User(name='Charlie White', email='charlie.white@example.com', password='password123', age=35, gender='Male'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(team_name='Team Alpha', created_at='2025-04-08')
        team2 = Team(team_name='Team Beta', created_at='2025-04-08')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Running', duration=30, calories_burned=300),
            Activity(user=users[1], activity_type='Cycling', duration=60, calories_burned=600),
            Activity(user=users[2], activity_type='Swimming', duration=45, calories_burned=450),
            Activity(user=users[3], activity_type='Yoga', duration=50, calories_burned=200),
            Activity(user=users[4], activity_type='Weightlifting', duration=40, calories_burned=400),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, total_points=100, rank=1),
            Leaderboard(team=team2, total_points=80, rank=2),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(workout_name='Morning Run', description='A quick morning run to start the day', difficulty_level='Easy'),
            Workout(workout_name='Cycling Session', description='An intense cycling session', difficulty_level='Medium'),
            Workout(workout_name='Swimming Laps', description='Swimming laps in the pool', difficulty_level='Hard'),
            Workout(workout_name='Yoga Routine', description='A relaxing yoga routine', difficulty_level='Easy'),
            Workout(workout_name='Weightlifting', description='Strength training with weights', difficulty_level='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
