from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data for OctoFit Tracker...')

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users (students)
        users_data = [
            {'email': 'mona.smith@mergington.edu', 'name': 'Mona Smith', 'password': 'secure123'},
            {'email': 'peter.parker@mergington.edu', 'name': 'Peter Parker', 'password': 'secure123'},
            {'email': 'diana.prince@mergington.edu', 'name': 'Diana Prince', 'password': 'secure123'},
            {'email': 'bruce.wayne@mergington.edu', 'name': 'Bruce Wayne', 'password': 'secure123'},
            {'email': 'clark.kent@mergington.edu', 'name': 'Clark Kent', 'password': 'secure123'},
            {'email': 'natasha.rogers@mergington.edu', 'name': 'Natasha Rogers', 'password': 'secure123'},
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(**user_data)
            users.append(user)
            self.stdout.write(f'Created user: {user.name}')

        # Create teams with themes
        teams_data = [
            {'name': 'Mergington Marathoners'},
            {'name': 'Fitness Phoenixes'},
            {'name': 'Wellness Warriors'},
        ]

        teams = []
        for i, team_data in enumerate(teams_data):
            team = Team.objects.create(**team_data)
            # Distribute users across teams (2 users per team)
            team.members.add(users[i*2], users[i*2 + 1])
            teams.append(team)
            self.stdout.write(f'Created team: {team.name}')

        # Create varied activities over past week
        activity_types = ['Running', 'Swimming', 'Cycling', 'Basketball', 'Yoga', 'Weight Training']
        now = timezone.now()
        
        for user in users:
            # Create 3-5 activities per user over the last week
            for _ in range(3):
                days_ago = timezone.timedelta(days=_)
                activity_data = {
                    'user': user,
                    'type': activity_types[_ % len(activity_types)],
                    'duration': 30 + (_ * 15),  # Varying durations
                    'date': now - days_ago
                }
                activity = Activity.objects.create(**activity_data)
                self.stdout.write(f'Created activity: {activity.type} by {activity.user.name}')

        # Create leaderboard with varying points
        for i, user in enumerate(users):
            points = 100 + (i * 25)  # Varying points for different users
            leaderboard = Leaderboard.objects.create(user=user, points=points)
            self.stdout.write(f'Created leaderboard entry for {user.name} with {points} points')

        # Create sample workouts
        workouts_data = [
            {
                'name': 'Morning Energy Boost',
                'description': '30-minute cardio routine: 10 min jogging, 10 min jumping jacks, 10 min high knees'
            },
            {
                'name': 'Strength Builder',
                'description': '45-minute routine: pushups, squats, lunges, planks'
            },
            {
                'name': 'Flexibility Focus',
                'description': '30-minute yoga and stretching routine'
            },
            {
                'name': 'Team Sports Mix',
                'description': '60-minute mixed sports activities: basketball, volleyball'
            },
            {
                'name': 'Endurance Challenge',
                'description': '40-minute circuit training with cardio intervals'
            }
        ]

        for workout_data in workouts_data:
            workout = Workout.objects.create(**workout_data)
            self.stdout.write(f'Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the OctoFit Tracker database with test data'))
