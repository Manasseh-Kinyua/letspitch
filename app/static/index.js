function deletePitch(pitchId) {
    fetch('/delete-pitch', {
        method: "POST",
        body: JSON.stringify({ pitchId: pitchId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}