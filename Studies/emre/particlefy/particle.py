import numpy as np
import math
import random as r
scale = 108000/3600




class Position():
    def __init__(self,x,y,h):
        '''
        :param x: x position
        :param y: y position
        :param h: height from sea level

        '''
        self.x = x
        self.y = y
        self.height = h


class Plane():
    def __init__(self,x,y,h):
        Position.__init__(self,x,y,h)

        self.measurements = []

    def move(self,theta_dot):
        '''
        :param theta_dot: angular velocity, enter 0 for moving straight

        '''

        self.x += theta_dot * math.cos(self.theta)
        self.y += theta_dot * math.sin(self.theta)


    def measure(self):
        '''
        We don't have multiple measurements, so we just pass this

        '''
        pass

    

class Particle():
    def __init__(self,x,y,h):
        Position.__init__(self,x,y,h)
        self.measurements = []
        self.weight = 0
        self.theta = 0
        self.interval = 0
        self.speed = 30
        self.scale = scale
        self.x_list = []
        self.y_list = []
        self.x_list.append(x)
        self.y_list.append(y)
        self.measurement_sigma =  100
        self.sum_prob = 0
    def move(self,speed):
        '''
        :param theta_dot: angular velocity, enter 0 for moving straight

        '''

        self.y += (speed) * math.cos(self.theta)
        self.x += (self.speed/scale) * math.sin(self.theta)
        if self.x or self.y > 3600:
            pass
        else: 
            self.x_list.append(self.x)
            self.y_list.append(self.y)


    def measure_height(self, data):
        '''
        
        :param scale: scale of the map
        :param data: dted 
        :param interval: interval for height data to accept
        :param speed: speed of the plane        
        '''
        if self.x or self.y > 3600:
            pass
        else:
            self.height = data[int(self.y),int(self.x)]

        #place particle next position on matplotlib


    def probability_density_function(self, mu, x):
        sigma = self.measurement_sigma

        #print(f"e'li ifade {1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * (((x-mu))/sigma)**2)}")
        #print(f"e'nin solu {1/(sigma*math.sqrt(2*math.pi))}")
        
        return 1/(sigma*math.sqrt(2*math.pi))*math.e**(-0.5 * ((x-mu)/sigma)**2)
    
    def update_weight(self, robot_height):
        #print(self.x, self.y)

        if self.x or self.y > 3600:
            pass
            #print(self.weight)
        
        self.weight = self.probability_density_function(robot_height,self.height)
        print(robot_height, self.height, self.weight)
        
        self.sum_prob += self.weight


    
    def resample_particles(particles,near_points):
        weights = []

        for particle in particles:
            weights += [particle.weight]
    
        print(sum(weights))
        #if (sum(weights)<0.05):
        #    resampled_particles=[]
        #    xy_min = np.min(np.min(near_points,axis=1),axis=0)
        #    xy_max = np.max(np.max(near_points,axis=1),axis=0)
        #    for i in range(len(particles)):
        #        resampled_particles += [Particle(r.uniform(low=xy_min,high=xy_max,size=(len(particles))))]
        #    return resampled_particles
    
    
        resample = r.choices(range(len(particles)), weights=weights, k=len(particles))
        #print(resample)
        #print(weights)
    
    
        resampled_particles = []
    
        for i in resample:
            resampled_particles += [Particle(particles[i].x,particles[i].y,100)]

        return resampled_particles




