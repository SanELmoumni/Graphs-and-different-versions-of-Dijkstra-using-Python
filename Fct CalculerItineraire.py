public String calculer() throws ClassNotFoundException, SQLException {
		getStationArretList();
		initialiser();
		for (StationArret st : stationArretList) {
			setSortie(true);

			if (depart == st.getStationDepId()
					&& (departList.contains(st.getStationDesId()) || arrive == st
							.getStationDesId())) {
				Pair temp = new Pair(depart, st.getStationDesId());
				System.out.println(temp.getA() + "  :  " + temp.getB());

				getPair().add(temp);
				time += st.getTemps();
				duplicateList(departList, temp, st, getPair(), getI(),
						getTime(), getSortie());

			}
			// depart=st.getStationDesId();
			// getPair().add(temp);
		}
		
		setTempsEffectue(getTempsList().get(
				getTempsList().indexOf(Collections.min(getTempsList()))));
		System.out.println("le meilleur temps est " + getTempsEffectue());
