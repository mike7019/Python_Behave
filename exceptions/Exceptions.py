from typing import Optional, Sequence


class Exceptions:
    class WebDriverException(Exception):
        def __init__(self, msg: Optional[str] = None, screen: Optional[str] = None,
                     stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg)
            self.msg = msg
            self.screen = screen
            self.stacktrace = stacktrace

    class ElementClickInterceptedException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "The Element Click command could not be completed because the element receiving the events is "
                   "obscuring the element that was requested to be clicked.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ElementNotInteractableException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "An element is present in the DOM but interactions with that element will hit another element due "
                   "to paint order.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ElementNotSelectableException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "Trying to select an unselectable element, for example, selecting a 'script' element.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ElementNotVisibleException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "An element is present on the DOM, but it is not visible, and so is not able to be interacted with. Most commonly encountered when trying to click or read text of an element that is hidden from view.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ImeActivationFailedException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Activating an IME engine has failed.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ImeNotAvailableException(WebDriverException):
        def __init__(self, msg: Optional[str] = "IME support is not available on the machine.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InsecureCertificateException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "Navigation caused the user agent to hit a certificate warning, usually the result of an expired or invalid TLS certificate.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidArgumentException(WebDriverException):
        def __init__(self, msg: Optional[str] = "The arguments passed to a command are either invalid or malformed.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidCookieDomainException(WebDriverException):
        def __init__(self,
                     msg: Optional[str] = "Attempting to add a cookie under a different domain than the current URL.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidCoordinatesException(WebDriverException):
        def __init__(self, msg: Optional[str] = "The coordinates provided to an interaction’s operation are invalid.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidElementStateException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "A command could not be completed because the element is in an invalid state. This can be caused by attempting to clear an element that isn’t both editable and resettable.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidSelectorException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "The selector used to find an element does not return a WebElement. This can happen when the selector is an xpath expression and it is either syntactically invalid or the expression does not select WebElements.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidSessionIdException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "The given session id is not in the list of active sessions, meaning the session either does not exist or that it’s not active.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class InvalidSwitchToTargetException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Frame or window target to be switched doesn’t exist.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class JavascriptException(WebDriverException):
        def __init__(self, msg: Optional[str] = "An error occurred while executing JavaScript supplied by the user.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class MoveTargetOutOfBoundsException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "The target provided to the ActionsChains move() method is invalid, i.e., out of document.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoAlertPresentException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Switching to no presented alert.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchAttributeException(WebDriverException):
        def __init__(self, msg: Optional[str] = "The attribute of element could not be found.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchCookieException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "No cookie matching the given path name was found amongst the associated cookies of the current browsing context’s active document.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchDriverException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Driver is not specified and cannot be located.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchElementException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Element could not be found.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchFrameException(InvalidSwitchToTargetException):
        def __init__(self, msg: Optional[str] = "Frame target to be switched doesn’t exist.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchShadowRootException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "Trying to access the shadow root of an element when it does not have a shadow root attached.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class NoSuchWindowException(InvalidSwitchToTargetException):
        def __init__(self, msg: Optional[str] = "Window target to be switched doesn’t exist.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class ScreenshotException(WebDriverException):
        def __init__(self, msg: Optional[str] = "A screen capture was made impossible.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class SessionNotCreatedException(WebDriverException):
        def __init__(self, msg: Optional[str] = "A new session could not be created.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class StaleElementReferenceException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "A reference to an element is now 'stale'. Possible causes include being no longer on the same page, the page may have refreshed, or the element may have been removed and re-added to the screen.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class TimeoutException(WebDriverException):
        def __init__(self, msg: Optional[str] = "A command does not complete in enough time.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class UnableToSetCookieException(WebDriverException):
        def __init__(self, msg: Optional[str] = "Driver fails to set a cookie.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class UnexpectedAlertPresentException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "An unexpected alert has appeared. Usually raised when an unexpected modal is blocking the webdriver from executing commands.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None,
                     alert_text: Optional[str] = None) -> None:
            super().__init__(msg, screen, stacktrace)
            self.alert_text = alert_text

    class UnexpectedTagNameException(WebDriverException):
        def __init__(self, msg: Optional[str] = "A support class did not get an expected web element.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    class UnknownMethodException(WebDriverException):
        def __init__(self, msg: Optional[
            str] = "The requested command matched a known URL but did not match any methods for that URL.",
                     screen: Optional[str] = None, stacktrace: Optional[Sequence[str]] = None) -> None:
            super().__init__(msg, screen, stacktrace)

    # Example Usage:
    try:
        # Code that may raise one of the above exceptions
        raise ElementClickInterceptedException()
    except WebDriverException as e:
        print(f"Caught WebDriverException: {e}")
        # Handle the exception as needed
