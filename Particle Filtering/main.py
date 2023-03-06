import math
import random

import numpy as np


class Station:
    def __init__(self, name, info, noise):
        self.name = name
        self.xyz = info
        self.noise = noise
        self.x = info[0]
        self.y = info[1]
        self.z = info[2]


def initial_station_info():
    dict_ = {
        "Copernicus": {"coordinates": [99, 198, -4], "noise_std": 15},
        "Montes": {"coordinates": [320, 545, 5], "noise_std": 10},
        "Ptolem": {"coordinates": [463, -181, -11], "noise_std": 80},
        "Albat": {"coordinates": [581, -233, 0], "noise_std": 80},
        "Lacus": {"coordinates": [680, 279, 0], "noise_std": 66},
        "Theophilus": {"coordinates": [1020, -230, -1], "noise_std": 15},
        "Luna21": {"coordinates": [1117, 509, 7], "noise_std": 40},
        "Amoris": {"coordinates": [1316, 388, 2], "noise_std": 35}
    }
    all_stations = []
    for x in dict_:
        new_ = Station(x, dict_[x]['coordinates'], dict_[x]['noise_std'])
        all_stations.append(new_)
    return all_stations


def calculate_x(d, first_angle, second_angle):
    first_angle = math.radians(first_angle)
    second_angle = math.radians(second_angle)
    return d * np.cos(first_angle) * np.cos(second_angle)


def calculate_y(d, first_angle, second_angle):
    first_angle = math.radians(first_angle)
    second_angle = math.radians(second_angle)
    return d * np.cos(first_angle) * np.sin(second_angle)


def calculate_z(d, first_angle):
    first_angle = math.radians(first_angle)
    return d * np.sin(first_angle)


def calculate_distance(new_x, new_y, new_z, xyz):
    x_prime = xyz[0]
    y_prime = xyz[1]
    z_prime = xyz[2]
    return math.sqrt((x_prime - new_x) ** 2 + (y_prime - new_y) ** 2 + (z_prime - new_z) ** 2)


def calculate_pdf(probable_dist, reported_distance, sigma):
    # from scipy.stats import norm
    # norm.ppf()

    return -1 * np.log(np.sqrt(2 * np.pi) * sigma) - ((probable_dist - reported_distance) ** 2) / (2 * sigma ** 2)


def replace_half_of_articles(all_weights, all_particles, parameter_of_covariance_matrix_for_prior, particle_num):
    indexes = list(np.flip(np.argsort(all_weights)))
    chosen = indexes[0:int(particle_num/2)]
    new_all_particles = []
    new_all_weights = []
    for index in chosen:
        new_all_particles.append(all_particles[index])
        new_all_weights.append(all_weights[index])

    new_all_particles = np.array(new_all_particles)

    for i in range(int(particle_num/2)):
        a = random.randint(0, int(particle_num/2) - 1)
        new_particles = np.random.multivariate_normal(new_all_particles[a],
                                                      np.array([[1, 0, 0], [0, 1, 0],
                                                                [0, 0, 1]]) * 0.1,  # mult by cov?
                                                      1)
        new_all_particles = np.concatenate((new_all_particles, new_particles), axis=0)
        new_all_weights.append(new_all_weights[a])

    return new_all_particles, new_all_weights


def main_answer(all_weights, all_particles, particle_num):
    indexes = list(np.flip(np.argsort(all_weights)))
    chosen = indexes[0:10]
    new_all_particles = []
    new_all_weights = []
    for index in chosen:
        new_all_particles.append(all_particles[index])
        new_all_weights.append(all_weights[index])
    new_all_weights = np.array(new_all_weights)
    new_all_weights = new_all_weights / sum(new_all_weights)
    # print(all_weights)
    # print(all_particles)
    answer = np.array([0.0, 0.0, 0.0])
    for i in range(len(chosen)):
        answer = new_all_weights[i] * np.array(new_all_particles[i]) + answer
    # for i in range(particle_num):
    #     answer = all_weights[i] * np.array(all_particles[i]) + answer
    return answer


def start(particle_num):
    dict_ = {"Copernicus": 0, "Montes": 1, "Ptolem": 2, "Albat": 3, "Lacus": 4, "Theophilus": 5, "Luna21": 6, "Amoris": 7}
    x_maybe, y_maybe, z_maybe = map(float, input().split(", "))
    d_parameter_of_exponential = float(input())
    parameter_of_covariance_matrix_for_prior = float(input())
    records_number = int(input())
    all_records = [[0.0] * records_number for i in range(8)]
    names_this_order = []
    for station in range(8):
        station_name = input()  # maybe needed
        names_this_order.append(station_name)
        for record in range(records_number):
            new_record = float(input())
            all_records[station][record] = new_record
    station_info = initial_station_info()
    all_particles = np.random.multivariate_normal([x_maybe, y_maybe, z_maybe],
                                                  np.array([[1, 0, 0], [0, 1, 0],
                                                            [0, 0, 1]]) * parameter_of_covariance_matrix_for_prior,
                                                  particle_num)  # بررسی ورودی
    # print(all_particles)

    for step in range(records_number):
        all_weights = [0 for i in range(particle_num)]
        for cnt in range(len(all_particles)):
            particle = all_particles[cnt]
            current_x = particle[0]
            current_y = particle[1]
            current_z = particle[2]
            d = np.random.exponential(scale=d_parameter_of_exponential, size=1)  # 1/d or d
            first_angle = np.random.uniform(low=-22.5, high=0.0, size=1)
            second_angle = np.random.uniform(low=-22.5, high=45.0, size=1)
            new_x = calculate_x(d, first_angle, second_angle) + current_x
            new_y = calculate_y(d, first_angle, second_angle) + current_y
            new_z = calculate_z(d, first_angle) + current_z
            # print(calculate_x(d, first_angle, second_angle))
            all_particles[cnt][0] = new_x
            all_particles[cnt][1] = new_y
            all_particles[cnt][2] = new_z
            for name in names_this_order:
                station_num = dict_[name]
                reported_distance = all_records[station_num][step]
                probable_dist = calculate_distance(new_x, new_y, new_z, station_info[station_num].xyz)
                sigma = station_info[station_num].noise
                p_of_pdf = calculate_pdf(probable_dist, reported_distance, sigma)

                all_weights[cnt] += p_of_pdf

            # all_weights.append(weight)
        if step == records_number - 1:
            return main_answer(all_weights, all_particles, particle_num)
        all_particles, all_weights = replace_half_of_articles(all_weights, all_particles,
                                                              parameter_of_covariance_matrix_for_prior, particle_num)  # Half ?


if __name__ == '__main__':
    answer = start(500)
    print(int(np.ceil(answer[0] / 100) * 100))
    print(int(np.ceil(answer[1] / 100) * 100))
    print(int(np.ceil(answer[2] / 100) * 100))
