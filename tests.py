import unittest
from user import create_user, login_user, logout_user
from post import create_post
from comment import post_comment
from message import send_message
from notification import notify_user
from search import search_content
from password_reset import reset_password
from email_verification import verify_email
from settings import update_settings
from report import report_content
from block import block_user
from follow import follow_user
from image_upload import upload_image
from video_upload import upload_video
from audio_upload import upload_audio
from event import create_event
from group import create_group
from page import create_page
from live_stream import start_live_stream
from poll import create_poll
from quiz import create_quiz
from payment import make_payment

class TestSocialMediaPlatform(unittest.TestCase):

    def setUp(self):
        self.current_user = create_user("test_user", "test_password", "test_email")

    def test_login_logout(self):
        login_user(self.current_user)
        self.assertTrue(self.current_user.is_logged_in)
        logout_user(self.current_user)
        self.assertFalse(self.current_user.is_logged_in)

    def test_create_post(self):
        post = create_post(self.current_user, "Test post")
        self.assertEqual(post.content, "Test post")

    def test_post_comment(self):
        post = create_post(self.current_user, "Test post")
        comment = post_comment(self.current_user, post, "Test comment")
        self.assertEqual(comment.content, "Test comment")

    def test_send_message(self):
        recipient = create_user("test_recipient", "test_password", "test_email")
        message = send_message(self.current_user, recipient, "Test message")
        self.assertEqual(message.content, "Test message")

    def test_notify_user(self):
        recipient = create_user("test_recipient", "test_password", "test_email")
        notification = notify_user(recipient, "Test notification")
        self.assertEqual(notification.content, "Test notification")

    def test_search_content(self):
        post = create_post(self.current_user, "Test post")
        results = search_content("Test post")
        self.assertIn(post, results)

    def test_reset_password(self):
        old_password = self.current_user.password
        reset_password(self.current_user, "new_password")
        self.assertNotEqual(self.current_user.password, old_password)

    def test_verify_email(self):
        self.assertFalse(self.current_user.email_verified)
        verify_email(self.current_user)
        self.assertTrue(self.current_user.email_verified)

    def test_update_settings(self):
        old_settings = self.current_user.settings
        update_settings(self.current_user, {"theme": "dark"})
        self.assertNotEqual(self.current_user.settings, old_settings)

    def test_report_content(self):
        post = create_post(self.current_user, "Test post")
        report = report_content(self.current_user, post, "Test report")
        self.assertEqual(report.content, "Test report")

    def test_block_user(self):
        user_to_block = create_user("test_block", "test_password", "test_email")
        block_user(self.current_user, user_to_block)
        self.assertIn(user_to_block, self.current_user.blocked_users)

    def test_follow_user(self):
        user_to_follow = create_user("test_follow", "test_password", "test_email")
        follow_user(self.current_user, user_to_follow)
        self.assertIn(user_to_follow, self.current_user.following)

    def test_upload_image(self):
        image_path = "test_image.jpg"
        image = upload_image(self.current_user, image_path)
        self.assertEqual(image.path, image_path)

    def test_upload_video(self):
        video_path = "test_video.mp4"
        video = upload_video(self.current_user, video_path)
        self.assertEqual(video.path, video_path)

    def test_upload_audio(self):
        audio_path = "test_audio.mp3"
        audio = upload_audio(self.current_user, audio_path)
        self.assertEqual(audio.path, audio_path)

    def test_create_event(self):
        event = create_event(self.current_user, "Test event", "Test location", "Test date")
        self.assertEqual(event.title, "Test event")

    def test_create_group(self):
        group = create_group(self.current_user, "Test group")
        self.assertEqual(group.name, "Test group")

    def test_create_page(self):
        page = create_page(self.current_user, "Test page")
        self.assertEqual(page.name, "Test page")

    def test_start_live_stream(self):
        live_stream = start_live_stream(self.current_user, "Test live stream")
        self.assertEqual(live_stream.title, "Test live_stream")

    def test_create_poll(self):
        poll = create_poll(self.current_user, "Test poll", ["Option 1", "Option 2"])
        self.assertEqual(poll.question, "Test poll")

    def test_create_quiz(self):
        quiz = create_quiz(self.current_user, "Test quiz", ["Question 1", "Question 2"])
        self.assertEqual(quiz.title, "Test quiz")

    def test_make_payment(self):
        payment = make_payment(self.current_user, 100)
        self.assertEqual(payment.amount, 100)

if __name__ == "__main__":
    unittest.main()