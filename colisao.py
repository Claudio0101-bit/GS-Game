from PPlay.collision import Collision


def colision(objetos, d_time):
    colisor = Collision()
    for i in range(len(objetos)):
        for j in range(len(objetos)):
            if i != j and (objetos[i].movable or objetos[i].playable) and colisor.collided(objetos[i].hit_box,objetos[j].hit_box):
                if (objetos[i].hit_box.x > objetos[j].hit_box.x and objetos[i].hit_box.x < objetos[j].hit_box.x + objetos[j].hit_box.width) and ((objetos[i].hit_box.y > objetos[j].hit_box.y and objetos[i].hit_box.y < objetos[j].hit_box.y + objetos[j].hit_box.height) or (objetos[i].hit_box.y + objetos[j].hit_box.height > objetos[j].hit_box.y and objetos[i].hit_box.y + objetos[i].hit_box.height < objetos[j].hit_box.y + objetos[j].hit_box.height)):
                    objetos[i].x += objetos[i].vel * d_time
                if (objetos[i].hit_box.x + objetos[i].hit_box.width > objetos[j].hit_box.x and objetos[i].hit_box.x + objetos[i].hit_box.width < objetos[j].hit_box.x + objetos[j].hit_box.width) and ((objetos[i].hit_box.y > objetos[j].hit_box.y and objetos[i].hit_box.y < objetos[j].hit_box.y + objetos[j].hit_box.height) or (objetos[i].hit_box.y + objetos[j].hit_box.height > objetos[j].hit_box.y and objetos[i].hit_box.y + objetos[i].hit_box.height < objetos[j].hit_box.y + objetos[j].hit_box.height)):
                    objetos[i].x -= objetos[i].vel * d_time
                if (objetos[i].hit_box.y > objetos[j].hit_box.y and objetos[i].hit_box.y < objetos[j].hit_box.y + objetos[j].hit_box.height) and ((objetos[i].hit_box.x > objetos[j].hit_box.x and objetos[i].hit_box.x < objetos[j].hit_box.x + objetos[j].hit_box.width) or (objetos[i].hit_box.x + objetos[j].hit_box.width > objetos[j].hit_box.x and objetos[i].hit_box.x + objetos[i].hit_box.width < objetos[j].hit_box.x + objetos[j].hit_box.width)):
                    objetos[i].y += objetos[i].vel * d_time
                if (objetos[i].hit_box.y + objetos[i].hit_box.height > objetos[j].hit_box.y and objetos[i].hit_box.y + objetos[i].hit_box.height < objetos[j].hit_box.y + objetos[j].hit_box.height) and ((objetos[i].hit_box.x > objetos[j].hit_box.x and objetos[i].hit_box.x < objetos[j].hit_box.x + objetos[j].hit_box.width) or (objetos[i].hit_box.x + objetos[j].hit_box.width > objetos[j].hit_box.x and objetos[i].hit_box.x + objetos[i].hit_box.width < objetos[j].hit_box.x + objetos[j].hit_box.width)):
                    objetos[i].y -= objetos[i].vel * d_time