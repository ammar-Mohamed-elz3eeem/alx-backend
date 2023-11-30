import redis, { createClient } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
	console.log(`Redis client not connected to the server: ${err.toString()}`)
);
client.on("connect", () => console.log(`Redis client connected to the server`));

export function addToHash(hashKey, fieldkey, fieldValue) {
	client.hset(hashKey, fieldkey, fieldValue, redis.print);
}

export function showHash(hashKey) {
	client.hgetall(hashKey, (err, reply) => console.log(reply));
}

const hash = {
	Portland: 50,
	Seattle: 80,
	"New York": 20,
	Bogota: 20,
	Cali: 40,
	Paris: 2,
};

for (const field in hash) {
	addToHash("HolbertonSchools", field, hash[field]);
}

showHash("HolbertonSchools");
