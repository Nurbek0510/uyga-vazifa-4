def ballni_ol(matn):
    try:
        ball = int(matn)
        return ball
    except ValueError:
        return "Ball son bo'lishi kerak"


print(ballni_ol("85"))
print(ballni_ol("sakson"))