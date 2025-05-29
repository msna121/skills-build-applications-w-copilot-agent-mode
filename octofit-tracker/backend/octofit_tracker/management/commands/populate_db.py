from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Create test users
        users_data = [
            {'email': 'john.doe@school.edu', 'name': 'John Doe', 'password': 'password123'},
            {'email': 'jane.smith@school.edu', 'name': 'Jane Smith', 'password': 'password123'},
            {'email': 'bob.wilson@school.edu', 'name': 'Bob Wilson', 'password': 'password123'},
        ]

        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(**user_data)
            users.append(user)
            self.stdout.write(f'Created user: {user.name}')

        # Create test teams
        teams_data = [
            {'name': 'Team Alpha'},
            {'name': 'Team Beta'},
        ]

        for i, team_data in enumerate(teams_data):
            team, created = Team.objects.get_or_create(**team_data)
            # Add members to teams
            if i == 0:
                team.members.add(users[0], users[1])
            else:
                team.members.add(users[1], users[2])
            self.stdout.write(f'Created team: {team.name}')

        # Create test activities
        activities_data = [
            {'user': users[0], 'type': 'Running', 'duration': 30, 'date': timezone.now()},
            {'user': users[1], 'type': 'Swimming', 'duration': 45, 'date': timezone.now()},
            {'user': users[2], 'type': 'Cycling', 'duration': 60, 'date': timezone.now()},
        ]

        for activity_data in activities_data:
            activity, created = Activity.objects.get_or_create(**activity_data)
            self.stdout.write(f'Created activity: {activity.type} by {activity.user.name}')

        # Create test leaderboard entries
        for user in users:
            leaderboard, created = Leaderboard.objects.get_or_create(user=user, defaults={'points': 100})
            self.stdout.write(f'Created leaderboard entry for: {leaderboard.user.name}')

        # Create test workouts
        workouts_data = [
            {'name': 'Morning Cardio', 'description': '30 minutes of running'},
            {'name': 'Strength Training', 'description': '45 minutes of weight lifting'},
            {'name': 'HIIT Workout', 'description': '20 minutes of high-intensity interval training'},
        ]

        for workout_data in workouts_data:
            workout, created = Workout.objects.get_or_create(**workout_data)
            self.stdout.write(f'Created workout: {workout.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
