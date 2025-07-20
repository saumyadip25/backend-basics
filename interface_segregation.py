"""
Interface Segregation Principle (ISP)
=====================================

The Interface Segregation Principle states that no client should be forced to depend 
on interfaces they don't use.

In simple terms: Don't force classes to implement methods they don't need.
Create smaller, focused interfaces instead of large, "fat" interfaces.

Simple Example: MP3Player vs MoviePlayer
"""

# ==========================================
# WRONG WAY - Violating ISP
# ==========================================

class MediaPlayer:
    """
    BAD EXAMPLE: Fat interface that forces all players to implement all methods
    
    Problems:
    - MP3Player doesn't need video methods
    - MoviePlayer doesn't need audio methods
    - Forces unnecessary implementations
    """
    
    def play_audio(self):
        raise NotImplementedError("Must implement play_audio")
    
    def play_video(self):
        raise NotImplementedError("Must implement play_video")
    
    def stop_video(self):
        raise NotImplementedError("Must implement stop_video")
    
    def adjust_video_brightness(self):
        raise NotImplementedError("Must implement adjust_video_brightness")


class MP3Player(MediaPlayer):
    """
    BAD EXAMPLE: MP3Player forced to implement video methods it doesn't need!
    
    Problems:
    - Only plays audio files
    - Forced to implement meaningless video methods
    - Violates ISP by depending on interfaces it doesn't use
    """
    
    def play_audio(self):
        return "Playing MP3 music..."
    
    # Forced to implement these even though MP3 player can't handle video!
    def play_video(self):
        raise Exception("MP3 Player cannot play video!")
    
    def stop_video(self):
        raise Exception("MP3 Player has no video to stop!")
    
    def adjust_video_brightness(self):
        raise Exception("MP3 Player cannot adjust video brightness!")


class MoviePlayer(MediaPlayer):
    """
    BAD EXAMPLE: MoviePlayer forced to implement audio methods it doesn't use!
    
    Problems:
    - Only plays video files
    - Forced to implement audio methods it doesn't need
    - Violates ISP by depending on interfaces it doesn't use
    """
    
    def play_video(self):
        return "Playing movie in high definition..."
    
    def stop_video(self):
        return "Movie playback stopped"
    
    def adjust_video_brightness(self):
        return "Video brightness adjusted"
    
    # Forced to implement this even though Movie player doesn't handle audio!
    def play_audio(self):
        raise Exception("Movie Player cannot play audio!")


# ==========================================
# RIGHT WAY - Following ISP
# ==========================================

class AudioPlayer:
    """Small, focused interface for audio functionality only"""
    
    def play_audio(self):
        raise NotImplementedError("Must implement play_audio")


class VideoPlayer:
    """Small, focused interface for video functionality only"""
    
    def play_video(self):
        raise NotImplementedError("Must implement play_video")
    
    def stop_video(self):
        raise NotImplementedError("Must implement stop_video")
    
    def adjust_video_brightness(self):
        raise NotImplementedError("Must implement adjust_video_brightness")


class MP3PlayerGood(AudioPlayer):
    """
    GOOD EXAMPLE: MP3Player only implements audio interface
    
    Benefits:
    - Only implements methods it actually needs
    - No confusing video method implementations
    - Clear and focused on audio functionality
    """
    
    def play_audio(self):
        return "Playing MP3 music with high quality sound..."


class MoviePlayerGood(VideoPlayer):
    """
    GOOD EXAMPLE: MoviePlayer only implements video interface
    
    Benefits:
    - Only implements methods it actually needs
    - No unnecessary audio method implementations
    - Clear and focused on video functionality
    """
    
    def play_video(self):
        return "Playing movie with excellent quality..."
    
    def stop_video(self):
        return "Movie playback stopped"
    
    def adjust_video_brightness(self):
        return "Movie brightness adjusted for perfect viewing"


# ==========================================
# USAGE EXAMPLES
# ==========================================

def demonstrate_isp_violation():
    """Show problems with fat interface"""
    print("=== VIOLATING ISP (BAD WAY) ===")
    
    mp3_player = MP3Player()
    movie_player = MoviePlayer()
    
    # MP3 player works for audio
    print(f"MP3 Player: {mp3_player.play_audio()}")
    
    # But fails when forced to handle video
    try:
        mp3_player.play_video()
    except Exception as e:
        print(f"ERROR: {e}")
    
    # Movie player works for video
    print(f"Movie Player: {movie_player.play_video()}")
    
    # But fails when forced to handle audio
    try:
        movie_player.play_audio()
    except Exception as e:
        print(f"ERROR: {e}")
    
    print("Problem: Players forced to implement methods they don't support!")
    print()


def demonstrate_isp_compliance():
    """Show benefits of segregated interfaces"""
    print("=== FOLLOWING ISP (GOOD WAY) ===")
    
    mp3_player = MP3PlayerGood()
    movie_player = MoviePlayerGood()
    
    # Each player only implements what it actually supports
    print("MP3 Player (audio only):")
    print(f"- {mp3_player.play_audio()}")
    
    print("\nMovie Player (video only):")
    print(f"- {movie_player.play_video()}")
    print(f"- {movie_player.stop_video()}")
    print(f"- {movie_player.adjust_video_brightness()}")
    
    print("\nBenefit: Each player only implements methods it actually supports!")
    print()


if __name__ == "__main__":
    demonstrate_isp_violation()
    demonstrate_isp_compliance()