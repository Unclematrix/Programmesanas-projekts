function deleteLesson(lessonId) {
    fetch('/delete-lesson', {
        method: 'POST',
        body: JSON.stringify({ lessonId: lessonId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}